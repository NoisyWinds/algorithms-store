var text = "this is a example";

function base64encode(text) {
  let code = '';
  let base64Code = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
  let res = '';

  for (let i of text) {
    let char = i.charCodeAt().toString(2);
    for (let a = 0; a <= 8 - char.length; a++) {
      char = 0 + char;
    }
    code += char
  }

  if (code.length % 24 === 8) {
    code += '0000';
    res += '=='
  }
  if (code.length % 24 === 16) {
    code += '00';
    res += '='
  }

  let encode = '';
  for (let i = 0; i < code.length; i += 6) {
    let item = code.slice(i, i + 6);
    encode += base64Code[parseInt(item, 2)];
  }

  return encode + res;
}

console.log(base64encode(text)); // dGhpcyBpcyBhIGV4YW1wbGU=
