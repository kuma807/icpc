import concurrent.futures
import subprocess
import time

#コードをコンパイルする(pythonなどの場合不要)
subprocess.run(f"g++ -o atcoder atcoder.cpp -std=c++17", shell=True)#要変更

start = time.time()

#パソコンのプロセス数
max_process = 16#要変更
proc_list = []
cnt = 0
subprocess.run(f"rm out/*", shell=True)
with open("input.txt") as f:
    l = f.readlines()
    index = 0
    while index < len(l):
        N = l[index]
        S = str(N) + "\n0"
        #自分のコードを実行するためのコマンド
        proc = subprocess.Popen(f"echo '{S}' | ./atcoder > out/{cnt}.txt", shell=True)#要変更
        cnt += 1
        index += 1
        proc_list.append(proc)

for subproc in proc_list:
    subproc.wait()

print("time: ", time.time() - start)
print("テストケース数(1-index):", cnt)
ans = ""
for i in range(cnt):
    with open(f"out/{i}.txt") as f:
        ans += f.read()

with open("output.txt", mode="w") as f:
    f.write(ans)
