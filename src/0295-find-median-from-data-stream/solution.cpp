#include<bits/extc++.h>

using namespace std;
using namespace __gnu_pbds;
using ll = long long;
using ull = unsigned long long int;
template <class T> using binary_tree = tree<T, null_type, less_equal<T>, rb_tree_tag, tree_order_statistics_node_update>; // allows duplicates, sorted ascending

class MedianFinder {
private:
    binary_tree<ll> data; // Using long long for larger number support

public:
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        data.insert(num); // Insert the number into the tree
    }
    
    double findMedian() {
        size_t size = data.size();
        if (size % 2 == 0) {
            // Even size: average the two middle elements
            ll first = *data.find_by_order(size / 2 - 1);
            ll second = *data.find_by_order(size / 2);
            return (first + second) / 2.0; // Cast to double to get the average
        } else {
            // Odd size: return the middle element
            return (double)*data.find_by_order(size / 2);
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
