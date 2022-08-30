// Written: Roos Lindeboom 30 aug 2022


// --- CSV ---
const fs = require("fs");
const { parse } = require("csv-parse");

fs.createReadStream("Assignment-1-File formats/Article files/Articles/Article.csv")
  .pipe(parse({ delimiter: ",", from_line: 2 }))
  .on("data", function (row) {
    console.log(row);
  })

// --- yaml ---
// read.js

const yaml = require('js-yaml');

try {
    let fileContents = fs.readFileSync('Assignment-1-File formats/Article files/Articles/Article.yaml', 'utf8');
    let data = yaml.load(fileContents);

    console.log(data);
} catch (e) {
    console.log(e);
}



