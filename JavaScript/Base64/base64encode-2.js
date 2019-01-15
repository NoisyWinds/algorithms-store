var text = "this is a example";

function base64encode(text) {
  let base64Code = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
  let res = '';
  let i = 0;

  while (i < text.length) {
    let char1,char2,char3,enc1,enc2,enc3,enc4;

    char1 = text.charCodeAt(i++);
    char2 = text.charCodeAt(i++);
    char3 = text.charCodeAt(i++);

    enc1 = char1 >> 2; // 取第 1 字节的前 6 位
    if (isNaN(char2)) {
      // 只有 1 字节的时候
      enc2 = ((char1 & 3) << 4) | (0 >> 4);
      // 第65个字符用来代替补位的 = 号
      enc3 = enc4 = 64;
    } else if (isNaN(char3)) {
      // 只有 2 字节的时候
      enc2 = ((char1 & 3) << 4) | (char2 >> 4);
      enc3 = ((char2 & 15) << 2) | (0 >> 6);
      enc4 = 64;
    }else{
      enc2 = ((char1 & 3) << 4) | (char2 >> 4); // 取第 1 个字节的后 2 位(3 = 11 << 4 = 110000) + 第 2 个字节的前 4 位
      enc3 = ((char2 & 15) << 2) | (char3 >> 6); // 取第 2 个字节的后 4 位 (15 = 1111 << 2 = 111100) + 第 3 个字节的前 2 位
      enc4 = char3 & 63; // 取最后一个字节的最后 6 位 (63 = 111111)
    }
    res += base64Code.charAt(enc1) + base64Code.charAt(enc2) + base64Code.charAt(enc3) + base64Code.charAt(enc4)
  }

  return res;
}

console.log(base64encode(text));
