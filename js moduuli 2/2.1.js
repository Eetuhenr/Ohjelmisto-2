let numbers = [];
for (let i = 0; i < 5; i++) {
    let input = prompt(`Enter number ${i + 1}:`);
    numbers.push(Number(input));
    console.log("Numbers in reverse order:");
for (let i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i]);}