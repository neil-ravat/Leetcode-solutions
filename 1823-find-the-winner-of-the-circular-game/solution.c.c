int findTheWinner(int n, int k) {
    int data[10000];
    int front = 0;
    int rear = -1;
    int size = 0;
 
    for (int i = 1; i <= n; i++) {
        rear = (rear + 1) % 10000;
        data[rear] = i;
        size++;
    }
 
    while (size > 1) {
        for (int i = 1; i < k; i++) {
            rear = (rear + 1) % 10000;
            data[rear] = data[front];
            front = (front + 1) % 10000;
        }
        front = (front + 1) % 10000; // Remove the k-th person
        size--;
    }
 
    return data[front];
}