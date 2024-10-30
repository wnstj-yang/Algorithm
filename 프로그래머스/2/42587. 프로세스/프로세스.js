function solution(priorities, location) {
    let answer = 0;
    const indexes = Array(priorities.length).fill().map((_, i) => i)
    while (true) {
        const prior = priorities.shift()
        const index = indexes.shift()
        if (prior < Math.max(...priorities)) {
            priorities.push(prior)
            indexes.push(index)
        } else {
            answer++
            if (index === location) {
                break
            }
        }
    }
    return answer;
}