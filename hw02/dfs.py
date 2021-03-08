def dfs(x,y):
    global N,M,ans,arr,fx,fy,next_step # 声明全局变量，为了方便使用
    if fx==x and fy==y: # 如果到了终点，路线结果+1，并返回继续搜索
        ans=ans+1
        return
    else:
        for i in range(len(next_step)): #向四个方向继续搜索
            next_x = x + next_step[i][0]  #继续搜索的横坐标
            next_y = y + next_step[i][1]  #继续搜索的纵坐标
            if next_x>0 and next_x<=N and next_y>0 and next_y<=M and 0==arr[next_x][next_y]: #判断这个坐标是否合理，不能越界，不能走之前走过的和障碍
                arr[next_x][next_y]=1 #这个位置能走，则在接下来不能走，所以标为1
                dfs(next_x,next_y) #继续搜索
                arr[next_x][next_y]=0  #搜索结束把这个位置恢复为能经过的状态   

if __name__=='__main__':
    N,M,T=list(map(int,input().strip().split()))#输入N,M,T----N为行，M为列，T为障碍总数。
    sx,sy,fx,fy=list(map(int,input().strip().split())) #起点坐标SX,SY，终点坐标FX,FY
    arr=[[0 for j in range(M+1)] for i in range(N+1)] # 建立(N+1)*(M+1)的矩阵地图,因为题目下表是从1开始，数组是0所以加1空出一行
    for i in range(T):
        x,y=list(map(int,input().strip().split()))
        arr[x][y]=1 #障碍位置标为1
    ans=0
    arr[sx][sy]=1 #将起点标为1，表示不能再一次经过
    next_step = [[-1,0],[1,0],[0,-1],[0,1]] #向上下左右四个方向
    dfs(sx,sy) #递归搜索
    print(ans)