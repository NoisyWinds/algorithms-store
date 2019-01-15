class Node {
  constructor(val){
    this.left = null;
    this.right = null;
    this.val = val;
  }
}

class Tree {
  insertNode(parent,val){
    // parent is the node to start from
    // val is where the node current placed
    if(val < parent.value) {
      // if isset left node
      if(parent.left) {
        this.insertNode(parent.left,val);
      } else {
        parent.left = new Node(val);
      }
    } else {
      if(parent.right) {
        this.insertNode(parent.right,val);
      } else {
        parent.right = new Node(val);
      }
    }
  }
}
