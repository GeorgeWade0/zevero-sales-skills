/**
 * Zevero sales skills - usage log receiver.
 * Paste into Extensions → Apps Script on a new Google Sheet, then Deploy → New deployment →
 * Web app, Execute as: Me, Who has access: Anyone. Put the web app URL in hooks/usage-endpoint.
 * Logs only: timestamp, rep email, skill, trigger (auto/slash), plugin version.
 */
function doPost(e) {
  var d = JSON.parse(e.postData.contents);
  if (!/^zevero-sales[\w-]*:[\w-]+$/.test(d.skill || '')) return ContentService.createTextOutput('ignored');
  var ss = SpreadsheetApp.getActive();
  var log = ss.getSheetByName('usage') || setup_();
  log.appendRow([new Date(d.ts), d.rep, d.skill.split(':')[0], d.skill.split(':')[1], d.trigger, d.version]);
  return ContentService.createTextOutput('ok');
}

function setup_() {
  var ss = SpreadsheetApp.getActive();
  var log = ss.insertSheet('usage');
  log.appendRow(['timestamp', 'rep', 'kit', 'skill', 'trigger', 'version']);
  log.setFrozenRows(1);
  var s = ss.insertSheet('summary');
  s.getRange('A1').setValue('Skill uses, last 30 days');
  s.getRange('A2').setFormula("=QUERY(usage!A:F,\"select D, count(D) where A > date '\"&TEXT(TODAY()-30,\"yyyy-mm-dd\")&\"' group by D order by count(D) desc label count(D) 'uses'\",1)");
  s.getRange('D1').setValue('Active reps, last 30 days');
  s.getRange('D2').setFormula("=QUERY(usage!A:F,\"select B, count(B) where A > date '\"&TEXT(TODAY()-30,\"yyyy-mm-dd\")&\"' group by B order by count(B) desc label count(B) 'uses'\",1)");
  s.getRange('G1').setValue('Weekly uses');
  s.getRange('G2').setFormula("=QUERY(ARRAYFORMULA({IF(usage!A2:A=\"\",,TEXT(usage!A2:A-WEEKDAY(usage!A2:A,3),\"yyyy-mm-dd\")),usage!D2:D}),\"select Col1, count(Col2) where Col1 is not null group by Col1 order by Col1 desc label Col1 'week', count(Col2) 'uses'\",0)");
  return log;
}
