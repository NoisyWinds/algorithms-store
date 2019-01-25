# Divide And Conquer 分治法
假如一个目标很难达成的话，不如就把它分成若干的小目标吧... 

> 一天小明去超市买了一袋零食，粗心的售货员没有将其中的一件商品消磁，这时如何才能比较有效率的断定
  哪一件零食才是没有消磁的零食呢？ 
   
一个很好的办法就是，取这带零食的一半过检验机，将发出警报的这一半继续分一半过机。这样，每一次的数量都会是
上一次的一半，最终可以确定到底是哪一个商品。比较起来一件件过机，效率大大的提高了。

## 二分查找
以上的这个故事讲述的就是，我们分治法的一种特殊情况，二分查找。在计算机上，遍历查找的时间复杂度是O(n)，
但二分查找的时间复杂度仅仅是 O(log2(n))，常常被用于树状结构查找。

## 分治法
分治法的核心思想就是，将原问题分解成小问题来求解，那么这类问题必须满足一下几个条件：
- 原问题可以被分解成性质类似的子问题
- 问题规模缩小后有利于得出结果
- 子问题的解能够协助原问题得到最终解
- 子问题互相独立，不存在依赖关系

下面，我们就举一个分治法的经典例子：

### 归并排序（merge-sort）
我们现在有一组数需要进行排序：
- [5,8,4,2,1,6,7,3]  

把它分解成若干个小数组进行对比：
- [5,8,4,2] [1,6,7,3]
- [5,8] [4,2] [1,6] [7,3]
  
 通过算法合并有序子序列就依次变成了：
 - [5,8] [2,4] [1,6] [3,7]
 - [2,4,5,8] [1,3,6,7]
 - [1,2,3,4,5,6,7,8]
 
 这就是归并排序核心思想，把排序问题变成了排序子序列然后合并有序子序列这个小问题了。
 那么如何合并子序列？
 
方法很简单。就是平时双指针的方式，就以[2,4,5,8] [1,3,6,7] 举例：

- 设置两个指针（i = 0，j = 0）分别为与开头 [**2**,4,5,8] [**1**,3,6,7]
- 因为 1 < 2 取 1 ，j 向后推一位 （i = 0，j = 1）[**2**,4,5,8] [1,**3**,6,7]
- 又因为 2 < 3 取 2，i 向后推一位 （i = 1，j = 1） [2,**4**,5,8] [1,**3**,6,7]
- ...

按指针位置两两对比，最终实现排序。

JavaScript 详细代码：
```javascript
  const arr = [5, 8, 4, 2, 1, 6, 7, 3];

  class MergeSort {

    constructor(arr) {
      // 开辟一个临时数组用于储存结果
      this.temp = [];
      this.arr = arr;
      this.sort(0, arr.length - 1);
      console.log(this.temp);
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

  new MergeSort(arr);
```
排序以上数组，一一对比需要（8 * 7 / 2）28 次，时间复杂度为 O(n^2) 而归并排序只需要对比 16 次，每次合并操作的时间复杂度为O(n)，
排序时间O(log2n), 一共的时间复杂度就是O(nlogn)。并且，比起一些排序算法来说，效率稳定。

## 最大子序和 (maximum-subarray)
这是一道 LeetCode 的题目：
[Jump link](https://leetcode.com/problems/maximum-subarray/submissions/)

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

例如:
```
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

这个问题也可以使用分治法解决：
```javascript
  function subMaxSubArray(nums, left, right) {
  
    if (left === right) return nums[left];
    // 取中间分割
    let mid = ~~((left + right) / 2);
    // 递归继续分割
    let left_val = subMaxSubArray(nums, left, mid);
    let right_val = subMaxSubArray(nums, mid + 1, right);
    
    // 取左侧最大值
    let mid_left = nums[mid], sum_left = nums[mid];
    for (let i = mid - 1; i >= left; i--) {
      sum_left += nums[i];
      mid_left = Math.max(mid_left,sum_left);
    }
    
    // 取右侧最大值
    let mid_right = nums[mid + 1], sum_right = nums[mid + 1];
    for (let j = mid + 2; j <= right; j++) {
      sum_right += nums[j];
      mid_right = Math.max(mid_right,sum_right);
    }
    
    // 取全部的和，三者求最大值
    let mid_val = mid_left + mid_right;
    return Math.max(left_val,right_val,mid_val);
  }

  var maxSubArray = function (nums) {
    return subMaxSubArray(nums, 0, nums.length - 1);
  };

  console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]));
```

## 总结

> 尽管我知道目标，但是如果我只看接下来的这一步，
我就能够避开恐慌和昏头转向。—— 莫顿·亨特 《走一步，再走一步》

既然已经明白了什么是分治法，接下来不如就去看看和分治法异曲同工的动态规划吧。
