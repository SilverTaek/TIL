interface Queue {
  readonly size: number;
  enqueue(value: string): void;
  dequeue(): string;
}

type QueueNode = {
  value: string;
  next?: QueueNode;
};

class QueueImpl implements Queue {
  private _size = 0;
  private head?: QueueNode;
  private tail?: QueueNode;

  get size() {
    return this._size;
  }

  enqueue(value: string) {
    const node: QueueNode = { value };
    if (this._size === 0) {
      this.head = node;
    } else {
      this.tail!.next = node;
    }
    this.tail = node;
    this._size++;
  }

  dequeue(): string {
    if (!this.head) throw new Error("queue is not Empty");
    if (this.head.value === this.tail?.value) {
      this.tail = undefined;
    }
    const next = this.head.next;
    const result = this.head.value;
    this.head = next;
    this._size--;
    return result;
  }
}

const queue = new QueueImpl();

queue.enqueue("rm");
queue.enqueue("rmrm");
queue.enqueue("rmrmrm");
queue.enqueue("rmrmrmrm");
queue.enqueue("rmrmrmrmrm");

while (queue.size !== 0) {
  console.log(queue.dequeue());
}
