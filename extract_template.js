const fs = require('fs');
const file = 'StepsAI Homepage (Standalone).html';
const html = fs.readFileSync(file, 'utf8');
const templateMatch = html.match(/<script type="__bundler\/template">\s*(.*?)\s*<\/script>/s);
if (templateMatch) {
  const template = JSON.parse(templateMatch[1]);
  fs.writeFileSync('unbundled_template.html', template);
  console.log('Wrote unbundled_template.html');
} else {
  console.log('No template found');
}
