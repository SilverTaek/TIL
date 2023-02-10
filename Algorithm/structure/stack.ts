interface Stack {
  readonly size: number;
  push(value: string): void;
  pop(): string;
}
type StackNode = {
  readonly value: string;
  readonly next?: StackNode;
};

class StackImpl implements Stack {
  private _size = 0;
  private head?: StackNode;
  get size() {
    return this._size;
  }
  push(value: string): void {
    const node: StackNode = { value, next: this.head };
    this.head = node;
    this._size++;
  }
  pop(): string {
    if (this.head == null) {
      throw new Error("Stack is Empty!!");
    }
    const node = this.head;
    this.head = node.next;
    return node.value;
  }
}

const stack = new StackImpl();

stack.push("rm");
stack.push("rm1");
stack.push("rm2");
stack.push("rm3");

while (stack.size !== 0) {
  console.log(stack.pop());
}
