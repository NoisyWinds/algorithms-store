## 什么是 Base64 ?

文章链接：[JavaScript 什么是 Base64 编码，如何实现 Base64 ?](https://zhuanlan.zhihu.com/p/51407418)

一句话可以概括。  
**base64 是一种用64个字符（1字节 = 8bit）来表示任意 8bit 位的二进制数据的方法。**
  
它的作用非常广泛，如迅雷下载的下载链接、前端的 dataURL、邮件传输等等。得益于用可见字符对二进制的直接转化，
使得base64可以无视平台，无视语言，无视网页编码准确无误的传递信息，非常便捷。

## Base64 的原理

之前我们提到，base64 编码来自于 64 个可见字符。如表所示：

| Value| Char| Value| Char| Value| Char|Value| Char|
| :---: |:---:| :---: |:---:| :---: |:---:|:---: |:---:|
|0  |A  |16 |Q  |32 |g  |48 |w  |
|1  |B  |17 |R  |33 |h  |49 |x  |
|2  |C  |18 |S  |34 |i  |50 |y  |
|3  |D  |19 |T  |35 |j  |51 |z  |
|4  |E  |20 |U  |36 |k  |52 |0  |
|5  |F  |21 |V  |37 |l  |53 |1  |
|6  |G  |22 |W  |38 |m  |54 |2  |
|7  |H  |23 |X  |39 |n  |55 |3  |
|8  |I  |24 |Y  |40 |o  |56 |4  |
|9  |J  |25 |Z  |41 |p  |57 |5  |
|10 |K  |26 |a  |42 |q  |58 |6  |
|11 |L  |27 |b  |43 |r  |59 |7  |
|12 |M  |28 |c  |44 |s  |60 |8  |
|13 |N  |29 |d  |45 |t  |61 |9  |
|14 |O  |30 |e  |46 |u  |62 |+  |
|15 |P  |31 |f  |47 |v  |63 |/  |

从上表可知 base64 一共只有2的6次方64个字符（6bit）。而实际上 1 bytes = 8bit，那么它是如何转化的呢？

1. 将所有字符转化为二进制形式：

```Javascript
  var text = "abc";
  var code = "";
  for(let i of text){
    // charCode
    let number = i.charCodeAt().toString(2);
    
    // 将 toString 前面省略的0补上
    for(let a = 0; a <= 8 - number.length;a++){
       number = 0 + number;
    }
    code += number
  }
```

2. 将二进制数据每 6bit 位替换成一个 base64 字符：

```Javascript
  // code 按 6bit 一组 011000 010110 001001 100011
  var base64Code = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
  let encode = '';
  for(let i = 0;i<code.length;i += 6){
    let number = code.slice(i,i+6);
    encode += base64Code[parseInt(number,2)];
  }
  console.log(encode); // YWJj
```

这一步其实已经完成了对 base64 的编码，我们成功的把 "abc" 转化成了 "YWJj"。但是，假如字节总数不能被 6 整除呢？
我们知道 6 和 8 的最小公倍数是 24，也就是说，我们必须找到 3 bytes 的数据，并它替换成 4 个 base64 字符。

3. 对不足 24 bit (也就是 3 bytes) 的情况进行特殊处理：

```javascript
  // 只有 1 字节的时候
  if(code.length % 24 === 8){
    // 补齐到 2*6 = 12 bit
    code += '0000';
    // 剩余缺失的 2 个 base64 字符用等号代替
    res += '=='
  }
  // 只有 2 字节的时候
  if(code.length % 24 === 16){
    // 补齐到 3 * 6 = 18 bit
    code += '00';
    // 剩余缺失的 1 个 base64 字符用等号代替
    res += '='
  }
```

以上，就是一次简单的 base64 编码过程了：

```javascript
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
```

我们对于这样的代码效率表示不满意，二进制的操作不应该转成字符串的加减来达到效果。

## 用位运算简单优化一下

二进制运算，并且不再拼接字符串,逻辑任然保持一致。

```javascript
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
```



