class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            newCar = [position[i], speed[i]]
            cars.append(newCar)
        cars.sort()
        cars.reverse()

        timeFinish = []
        for car in cars:
            timeFinish.append((target - car[0]) / car[1])
        
        ans = 1
        for i in range(1, len(cars)):
            if timeFinish[i] <= timeFinish[i - 1]:
                timeFinish[i] = timeFinish[i - 1]
            else:
                ans += 1
        
        return ans
