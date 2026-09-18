
# № 1. Друк рядка у зворотньому порядку
def print_reverse(s):
    if s == "":
        return
    print_reverse(s[1:])
    print(s[0], end="")


def task1_demo():
    print("Завдання 1: реверс рядка")
    print_reverse("tiger")
    print() 
    print()


# № 2. Обмін сусідніх вузлів у зв'язаному списку
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head):
    if head is None or head.next is None:
        return head

    second = head.next
    head.next = swap_pairs(second.next)
    second.next = head
    return second


# Допоміжні функції (використано цикл, бо це не сама задача, а підготовка даних)
def build_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def list_to_str(head):
    def helper(node):
        if node is None:
            return "[]"
        if node.next is None:
            return f"[{node.val}]"
        rest = helper(node.next)
        return f"[{node.val}, " + rest[1:]
    return helper(head)


def task2_demo():
    print("Завдання 2: обмін сусідніх вузлів")
    for values in ([1, 2, 3, 4], [], [1]):
        head = build_list(values)
        new_head = swap_pairs(head)
        print(f"Input: {values} -> Output: {list_to_str(new_head)}")
    print()


# № 3. Числа Фібоначчі
def fibonacci(n):
    """
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2) для n > 1
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def task3_demo():
    print("Завдання 3: числа Фібоначчі")
    for n in (2, 3, 4, 5, 6, 7):
        print(f"F({n}) = {fibonacci(n)}")
    print()


# № 4. Сходинки (Climbing Stairs)
def climb_stairs(n, memo=None):
# memo — кеш уже пораховних результатів (n до 45, без нього наївна
# рекурсія дає забагато повторних викликів). Не бібліотека — лише
# оптимізація власної рекурсивної функції.
    if memo is None:
        memo = {}

    if n == 1:
        return 1
    if n == 2:
        return 2

    if n in memo:
        return memo[n]

    result = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    memo[n] = result
    return result


def task4_demo():
    print("Завдання 4: сходинки")
    for n in (2, 3, 7, 22, 45):
        print(f"n = {n} -> {climb_stairs(n)} способів")
    print()

# № 5. Піднесення до степеня pow(x, n)
def my_pow(x, n):
    if n < 0:
        return 1 / my_pow(x, -n)

    if n == 0:
        return 1.0

    half = my_pow(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return half * half * x


def task5_demo():
    print("Завдання 5: піднесення до степеня")
    tests = [(2.00000, 10), (2.10000, 3), (2.00000, -2)]
    for x, n in tests:
        print(f"x = {x}, n = {n} -> {round(my_pow(x, n), 5)}")
    print()




if __name__ == "__main__":
    task1_demo()
    task2_demo()
    task3_demo()
    task4_demo()
    task5_demo()
