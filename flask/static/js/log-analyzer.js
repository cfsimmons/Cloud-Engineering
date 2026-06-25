let allEntries = [];
let currentFilter = 'all';
let selectedIdx = null;

const SAMPLE = `[2024-03-12 08:14:22] INFO  Server started on port 3000
[2024-03-12 08:14:23] INFO  Database connection established
[2024-03-12 08:14:45] WARN  Deprecated API endpoint /v1/users called from 192.168.1.42
[2024-03-12 08:15:01] ERROR TypeError: Cannot read properties of undefined (reading 'userId')
    at AuthMiddleware.verify (/app/middleware/auth.js:34:18)
    at Layer.handle (/app/node_modules/express/lib/router/layer.js:95:5)
    at next (/app/node_modules/express/lib/router/route.js:137:13)
[2024-03-12 08:15:01] ERROR Request failed: GET /api/profile — 500 Internal Server Error
[2024-03-12 08:15:09] WARN  Memory usage at 87% (threshold: 80%)
[2024-03-12 08:16:02] DEBUG Fetching user record id=9214 from cache
[2024-03-12 08:16:03] INFO  Cache miss — querying database
[2024-03-12 08:16:44] ERROR UnhandledPromiseRejectionWarning: MongooseError: Operation 'users.findOne()' buffering timed out after 10000ms
    at Timeout.<anonymous> (/app/node_modules/mongoose/lib/drivers/node-mongodb-native/collection.js:175:23)
    at listOnTimeout (node:internal/timers:573:17)
[2024-03-12 08:16:44] ERROR Process exiting with code 1
[2024-03-12 08:17:01] INFO  Server restarted (auto-recovery)
[2024-03-12 08:17:15] WARN  Rate limit exceeded for IP 10.0.0.5 (120 req/min)
[2024-03-12 08:18:30] INFO  Scheduled job 'cleanup_sessions' completed in 340ms`;

function parseLevel(line) {
  const u = line.toUpperCase();
  if (/\b(ERROR|EXCEPTION|CRITICAL|FATAL|UNCAUGHT|UNHANDLED)\b/.test(u)) return 'error';
  if (/\b(WARN|WARNING)\b/.test(u)) return 'warn';
  if (/\b(INFO|INFORMATION|SUCCESS)\b/.test(u)) return 'info';
  if (/\b(DEBUG|TRACE|VERBOSE)\b/.test(u)) return 'debug';
  return 'log';
}

function parseTimestamp(line) {
  const m = line.match(/\d{4}[-/]\d{2}[-/]\d{2}[\sT]\d{2}:\d{2}(:\d{2})?/);
  return m ? m[0] : null;
}

function parseSource(line) {
  const m = line.match(/\(([^)]+\.(js|ts|py|java|rb|go|cs):\d+)\)/);
  return m ? m[1] : null;
}

function parse(raw) {
  const lines = raw.split('\n');
  const entries = [];
  let current = null;

  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed) continue;

    const isStack = /^\s*(at |File "|Traceback|\.\.\.)/.test(line);

    if (isStack && current) {
      current.stack = current.stack || [];
      current.stack.push(trimmed);
    } else {
      if (current) entries.push(current);
      current = {
        raw: trimmed,
        level: parseLevel(trimmed),
        ts: parseTimestamp(trimmed),
        src: parseSource(trimmed),
        message: trimmed
          .replace(/\[\d{4}[-/]\d{2}[-/]\d{2}[\sT]\d{2}:\d{2}(:\d{2})?\]/g, '')
          .replace(/\b(ERROR|WARN|WARNING|INFO|DEBUG|TRACE|CRITICAL|FATAL)\b\s*/i, '')
          .replace(/^\s*[-|:]\s*/, '')
          .trim() || trimmed,
        stack: null
      };
    }
  }

  if (current) entries.push(current);
  return entries;
}

function levelClass(l) {
  return { error: 'level-error', warn: 'level-warn', info: 'level-info', debug: 'level-debug', log: 'level-log' }[l] || 'level-log';
}

function levelLabel(l) {
  return { error: 'ERROR', warn: 'WARN', info: 'INFO', debug: 'DEBUG', log: 'LOG' }[l] || l.toUpperCase();
}

function escHtml(s) {
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function renderFiltered() {
  const search = document.getElementById('searchInput').value.toLowerCase();
  const list = document.getElementById('logList');

  const visible = allEntries.filter((e, i) => {
    const filterOk = currentFilter === 'all' || e.level === currentFilter;
    const searchOk = !search || e.message.toLowerCase().includes(search) || (e.raw && e.raw.toLowerCase().includes(search));
    return filterOk && searchOk;
  });

  if (!visible.length) {
    list.innerHTML = '<div class="no-results">No entries match current filter</div>';
    return;
  }

  list.innerHTML = visible.map((e, vi) => {
    const origIdx = allEntries.indexOf(e);
    return `<div class="log-entry${selectedIdx === origIdx ? ' selected' : ''}" onclick="selectEntry(${origIdx})">
      <span class="log-level ${levelClass(e.level)}">${levelLabel(e.level)}</span>
      <div class="log-body">
        <div class="log-message">${escHtml(e.message)}</div>
        <div class="log-meta">
          ${e.ts ? `<span class="log-ts">${e.ts}</span>` : ''}
          ${e.src ? `<span class="log-src">${escHtml(e.src)}</span>` : ''}
          ${e.stack ? `<span class="log-src" style="color:var(--red)">+${e.stack.length} frame${e.stack.length>1?'s':''}</span>` : ''}
        </div>
      </div>
    </div>`;
  }).join('');
}

function selectEntry(idx) {
  selectedIdx = idx;
  const e = allEntries[idx];
  const dp = document.getElementById('detailPanel');
  const dc = document.getElementById('detailContent');

  let html = `<div class="detail-line">${escHtml(e.raw)}</div>`;

  if (e.stack && e.stack.length) {
    html += `<div style="margin-top:8px; font-size:11px; color:var(--muted); font-family:var(--mono)">Stack trace:</div>`;
    html += e.stack.map((f, i) =>
      `<div class="detail-line"><span class="stack-frame${i===0?' first':''}">${escHtml(f)}</span></div>`
    ).join('');
  }

  dc.innerHTML = html;
  dp.classList.add('visible');
  renderFiltered();
}

function setFilter(f, btn) {
  currentFilter = f;
  document.querySelectorAll('.filter-btn').forEach(b => {
    b.className = 'filter-btn';
  });
  const cls = { all: 'active-all', error: 'active-error', warn: 'active-warn', info: 'active-info', debug: 'active-info' }[f] || '';
  if (cls) btn.classList.add(cls);
  renderFiltered();
}

function analyze() {
  const raw = document.getElementById('logInput').value.trim();
  if (!raw) return;

  allEntries = parse(raw);
  selectedIdx = null;

  const counts = { error: 0, warn: 0, info: 0, debug: 0, log: 0 };
  allEntries.forEach(e => counts[e.level]++);

  document.getElementById('cntError').textContent = counts.error;
  document.getElementById('cntWarn').textContent = counts.warn;
  document.getElementById('cntInfo').textContent = counts.info + counts.debug + counts.log;
  document.getElementById('cntTotal').textContent = allEntries.length;

  document.getElementById('emptyState').style.display = 'none';
  const rv = document.getElementById('resultsView');
  rv.style.display = 'flex';

  document.getElementById('detailPanel').classList.remove('visible');
  document.getElementById('searchInput').value = '';
  currentFilter = 'all';
  document.querySelectorAll('.filter-btn').forEach(b => b.className = 'filter-btn');
  document.querySelector('[data-filter="all"]').classList.add('active-all');

  renderFiltered();
}

function loadSample() {
  document.getElementById('logInput').value = SAMPLE;
  analyze();
}

function clearAll() {
  document.getElementById('logInput').value = '';
  allEntries = [];
  selectedIdx = null;
  document.getElementById('emptyState').style.display = 'flex';
  document.getElementById('resultsView').style.display = 'none';
  document.getElementById('detailPanel').classList.remove('visible');
}
