var MedianFinder = function() {
    // to find median in O(1) time, we will split all numbers coming in into
    // 2 Priority Queues - all input from lowest -> median will be stored in 
    // max, and all input from median -> highest will be stored in min. this
    // means that the .front().element of min and max will be in the middle.

    const max = new MaxPriorityQueue();
    const min = new MinPriorityQueue();
    // const tes = new Queue()
    
    return { addNum, findMedian }
    
    function addNum(num) {
        if (min.front() != null && num < min.front().element)
            max.enqueue(num)
        else
            min.enqueue(num)
        
        const diff = min.size() - max.size()
        if (diff > 1) 
            max.enqueue(min.dequeue().element)
        if (diff < -1) 
            min.enqueue(max.dequeue().element)
    }
    
    function findMedian() {
        const diff = min.size() - max.size()
        if (diff > 0)
            return min.front().element
        else if (diff < 0)
            return max.front().element
        else
            return (min.front().element + max.front().element)/2
    }
}
