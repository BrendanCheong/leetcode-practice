function searchRange(nums: number[], target: number): number[] {
    return [searchFirstLeft(nums, target), searchFirstRight(nums, target)]
}

const searchFirstLeft = (A: number[], target: number): number => {
    let left: number = 0, right: number = A.length - 1
    while (left <= right) {
        let mid: number = Math.floor((left + right) / 2)
        if (A[mid] < target) {
            left = mid + 1
        } else if (A[mid] > target) {
            right = mid - 1
        } else {
            if (mid - 1 < 0) {
                return mid
            } else if (A[mid - 1] != target) {
                return mid
            } else {
                right = mid - 1
            }
        }
    }
    return -1
}

function searchFirstRight(A: number[], target: number): number {
    let left: number = 0, right: number = A.length - 1
    while (left <= right) {
        let mid: number = Math.floor((left + right) / 2)
        if (A[mid] < target) {
            left = mid + 1
        } else if (A[mid] > target) {
            right = mid - 1
        } else {
            if (mid + 1 > A.length - 1) {
                return mid
            } else if (A[mid + 1] != target) {
                return mid
            }
            left = mid + 1
        }
    }
    return -1
}
