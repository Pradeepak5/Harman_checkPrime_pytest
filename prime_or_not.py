def check_prime(num):
    flag = False

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break

    # check if flag is True
    if flag:
        return False
    else:
        return True

if __name__=="__main__":
    num=int(input("Enter the num :"))
    result=check_prime(num)
    print(result)
