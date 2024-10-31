function solution(prices) {
    const answer = [];
    for (let i = 0; i < prices.length - 1; i++) {
        const num = prices[i]
        let cnt = 0
        for (let j = i + 1; j < prices.length; j++) {
            cnt++
            if (num > prices[j]) break
            
        }
        answer.push(cnt)
    }
    answer.push(0)
    return answer;
}