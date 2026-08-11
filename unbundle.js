const fs = require('fs');
const zlib = require('zlib');
const path = require('path');

const file = 'StepsAI Homepage (Standalone).html';
const html = fs.readFileSync(file, 'utf8');
const manifestMatch = html.match(/<script type="__bundler\/manifest">\s*(\{.*?\})\s*<\/script>/s);
if (!manifestMatch) {
  console.log("No manifest found");
  process.exit(1);
}

const manifest = JSON.parse(manifestMatch[1]);
const outDir = 'unbundled';
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir);

for (const [uuid, entry] of Object.entries(manifest)) {
  const buf = Buffer.from(entry.data, 'base64');
  let data = buf;
  if (entry.compressed) {
    try {
      data = zlib.gunzipSync(buf);
    } catch(e) {
      console.error('Failed to gunzip', uuid);
      continue;
    }
  }
  
  let ext = '.bin';
  if (entry.mime.includes('javascript')) ext = '.js';
  else if (entry.mime.includes('html')) ext = '.html';
  else if (entry.mime.includes('css')) ext = '.css';
  else if (entry.mime.includes('json')) ext = '.json';
  
  fs.writeFileSync(path.join(outDir, uuid + ext), data);
  console.log('Wrote', uuid + ext);
}
console.log("Done");
