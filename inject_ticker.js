const fs = require('fs');
let html = fs.readFileSync('StepsAI_Final.html', 'utf8');

const tickerCss = `
@keyframes tickerSlide { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
.ticker-container { overflow: hidden; white-space: nowrap; padding: 20px 0; background: rgba(0,0,0,0.1); border-top: 1px solid rgba(255,255,255,0.05); margin-top: 40px; }
.ticker-track { display: inline-block; animation: tickerSlide 20s linear infinite; }
.ticker-item { display: inline-block; font-family: 'Geist Mono', monospace; font-size: 14px; font-weight: 500; color: #6FA5F7; letter-spacing: 0.1em; margin-right: 40px; }
`;

html = html.replace('</style>', tickerCss + '</style>');

const tickerHtml = '<div class="ticker-container"><div class="ticker-track">' + Array(10).fill('<span class="ticker-item">ORDER · BOOKED · LEAD · RESOLVED</span>').join('') + '</div></div>';

html = html.replace('Your next customer is already on the way.</h2>', 'Your next customer is already on the way.</h2>' + tickerHtml);

fs.writeFileSync('StepsAI_Final.html', html);
console.log('Done');
