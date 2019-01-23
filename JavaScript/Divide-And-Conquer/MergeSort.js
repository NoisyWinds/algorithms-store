
class MergeSort {

  constructor(arr) {
    // 开辟一个临时数组用于储存结果
    this.temp = [];
    this.arr = arr;
    this.sort(0, arr.length - 1);
    return this.temp;
  }

  sort(left, right) {
    if (left < right) {
      let middle = ~~((left + right) / 2);
      this.sort(left, middle); // 递归排序左数组
      this.sort(middle + 1, right); // 递归排序右数组
      this.merge(left, middle, right);
    }
  }

  merge(left, middle, right) {
    let i = left; //左指针
    let j = middle + 1;//右指针
    let t = 0; //temp 数组指针
    while (i <= middle && j <= right) {
      if (this.arr[i] <= this.arr[j]) {
        this.temp[t++] = this.arr[i++];
      } else {
        this.temp[t++] = this.arr[j++];
      }
    }
    while (i <= middle) {//将左边剩下的元素填充进 temp 中
      this.temp[t++] = this.arr[i++];
    }
    while (j <= right) {//将右边剩下的元素填充进 temp 中
      this.temp[t++] = this.arr[j++];
    }
    t = 0;
    while (left <= right) {
      this.arr[left++] = this.temp[t++];
    }
  }
}
