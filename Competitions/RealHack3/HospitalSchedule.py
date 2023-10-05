import math

patient = input()

n = int(input())
p = int(input())

patients = input().split()
patients.append(patient)

patients = sorted(patients)

print((math.ceil((patients.index(patient)+1)/n))*20)