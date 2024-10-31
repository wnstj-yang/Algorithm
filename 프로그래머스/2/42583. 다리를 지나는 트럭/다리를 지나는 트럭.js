function solution(bridge_length, weight, truck_weights) {
    let answer = 0;
    const queue = Array(bridge_length).fill(0)
    while (queue.length > 0) {
        answer++;
        queue.shift()
        if (truck_weights.length > 0) {
            const sum = queue.reduce((a, b) => a + b, 0)
            if (sum + truck_weights[0] > weight) {
                queue.push(0)
            } else {
                queue.push(truck_weights.shift())
            }
        }
    }
    return answer;
}