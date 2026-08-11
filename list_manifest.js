const fs = require('fs');
const file = 'StepsAI Homepage (Standalone).html';
const html = fs.readFileSync(file, 'utf8');
const manifestMatch = html.match(/<script type="__bundler\/manifest">\s*(\{.*?\})\s*<\/script>/s);
const manifest = JSON.parse(manifestMatch[1]);
for (const [uuid, entry] of Object.entries(manifest)) {
  console.log(uuid, entry.mime);
}
