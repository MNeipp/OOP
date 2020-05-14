import unittest

# function I'm testing
def reverseList(list):
    for i in range (int(len(list)/2)):
        list[i],list[len(list)-1-i] = list[len(list)-1-i],list[i]
    return list

def isPalindrome(string):
    backwards = string[::-1]
    if backwards == string:
        return True
    else:
        return False

def coins(total_amount):
    change = [0,0,0,0]
    counting = 0
    while counting < total_amount:
        if counting + 0.25 <= total_amount:
            counting += 0.25
            change[0] += 1 
        elif counting + 0.1 <= total_amount:
            counting += 0.1
            change[1] += 1
        elif counting + .05 <= total_amount:
            counting += .05
            change[2] +=1
        elif counting + .01 <= total_amount:
            counting +=.01
            change[3] +=1  
    return change

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else: 
        return num * factorial(num-1)
    return num

def fibonacci(num):
    if num == 1 or num == 0:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)


#Tests I'm running

class reverseListTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([1,2,3]), [3,2,1])
    
    def testTwo(self):
        self.assertEqual(reverseList([1,2,3,4]), [4,3,2,1])

    def testThree(self):
        self.assertEqual(reverseList([1,"boobs",2, "butt"]), ["butt",2,"boobs",1])
    
    def testFour(self):
        self.assertEqual(reverseList([4,2,True,"apple",99]), [99,"apple",True,2,4])

class isPalindromeTests(unittest.TestCase):
    def testOne(self):
        self.assertTrue(isPalindrome("racecar"))
    def testTwo(self):
        self.assertFalse(isPalindrome("mason"))
    def testThree(self):
        self.assertEqual(isPalindrome("butter"), False)
    def testFour(self):
        self.assertEqual(isPalindrome("bloolb"), True)
    def testFive(self):
        self.assertTrue(isPalindrome("amanaplanacanalpanama"))

class changeTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coins(.75), [3,0,0,0])
    def testTwo(self):
        self.assertEqual(coins(1.55), [6,0,1,0])
    def testThree(self):
        self.assertEqual(coins(.04), [0,0,0,4])
    def testFour(self):
        self.assertEqual(coins(.14),[0,1,0,4])

class factorialTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(factorial(5), 120)
    def testTwo(self):
        self.assertEqual(factorial(4), 24)
    def testThree(self):
        self.assertEqual(factorial(3), 6)
    def testFour(self):
        self.assertEqual(factorial(6), 720)

class fibonacciTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fibonacci(1), 1)
    def testTwo(self):
        self.assertEqual(fibonacci(2), 1)
    def testThree(self):
        self.assertEqual(fibonacci(3), 2)
    def testFour(self):
        self.assertEqual(fibonacci(4), 3)
    def testFive(self):
        self.assertEqual(fibonacci(5), 5)
    def testSix(self):
        self.assertEqual(fibonacci(6), 8)
    def testSeven(self):
        self.assertEqual(fibonacci(7), 13)



if __name__ == "__main__":
    unittest.main()



