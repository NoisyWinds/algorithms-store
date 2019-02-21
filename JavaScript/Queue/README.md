# Queue and Stack 队列和栈
> 排队可以用来解决过于拥堵的问题，这便是队列的用途。

## 队列是什么？

这时候，我们可以想想我们是怎么排队的，比如有 3 个人在机场准备安检：
- [1,2,3]  

这时，来了第 4 个人，那么他需要排在最后： 
- [1,2,3,4]  

第 1 个人进了安检通道，队伍少了一个人：
- [2,3,4] 

很简单对吧，这就是队列。队列是一种数据结构，它的要点就是**先进先出**，就和排队一样，
每次执行优先取队列头部的数据，每次插入数据只能从队列的尾部插入。先被插入的数据先被执行，这就是队列。

理论上是这么说不错，然而实际工作上，它老是会被和栈混为一谈。

## 什么是栈？
这里讲的不是内存中的堆栈，而是栈这一种数据结构。它和队列不同的就是它的要点是**先进后出**，后入栈的数据会被优先处理。

你手上已经有 3 个任务了：
- [1,2,3]

老板有给了你 1 个加急任务：
- [1,2,3,4]

完成了加急任务后，你还得继续完成自己的任务：
- [1,2,3]


## 如何实现队列和栈
Js 实现起来太容易不过了...
```javascript
// queue 队列
var queue = [1,2,3];
queue.push(4);
while(queue.length > 0){
  let item = queue.unshift();
}

// stack 栈
var stack = [1,2,3];
stack.push(4); // 此为入栈
while(stack.length > 0){
  let item = stack.pop(); // 此为出栈
}
```
链表的方式来实现：
```javascript
function List(val) {
  this.val = val;
  this.next = null;
}
function Queue(arr) {
  if (!arr) return;
  let q = new List(arr[0]);
  let temp = q;
  for(let i = 1; i < arr.length;i++){
    temp.next = new List(arr[i]);
    temp = temp.next;
  }
  return q;
}
let queue = Queue([1,2,3,4]);

while(queue){
  queue = queue.next;
}
```

优点就是，在一些不会自动分配数组长度的语言中，不会造成溢出。








