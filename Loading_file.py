import time
from statemachine import StateMachine, State
Process=1


#Freespace=[False, False, False]
class Loading(StateMachine):
    Wait_forSignal=State('Waiting', initial=True)
    Pick_detail=State('Picking')
    Load_detail=State('Loading detail')
    Drop_detail=State('Dropping')
    Check_isFreespace=State('Checking freespace')
    Done=State('Process Done')
    place = 0

    waitTime=[1,2,3]

    wait=Wait_forSignal.to(Wait_forSignal)
    start_process=Wait_forSignal.to(Check_isFreespace)
    Pick=Check_isFreespace.to(Pick_detail)
    Load=Pick_detail.to(Load_detail)
    Drop=Load_detail.to(Drop_detail)
    Continue=Drop_detail.to(Check_isFreespace)
    EndProcess=Check_isFreespace.to(Done)
    Reset=Done.to(Wait_forSignal)

    def work_wait(self, i):
        time.sleep(self.waitTime[i])

    def on_enter_Check_isFreespace(self):
        print("Checking positioner...")
        Freespace=[True, True, True]
        self.work_wait(0)
        if (True in Freespace):
            for x in range(0, 3):
                if Freespace[x] == True:
                    Freespace[x]=False
                    place = x + 1
                    loading.Pick()
                    break
        else:
            loading.EndProcess()

    def on_enter_Pick_detail(self):
        print("Picking detail")
        self.work_wait(1)
        loading.Load()

    def on_enter_Load_detail(self):
        print("Loading detail to position ")
        self.work_wait(2)
        loading.Drop()

    def on_enter_Drop_detail(self):
        print("Dropping detail")
        self.work_wait(1)

    def on_enter_Done(self):
        print("Loading done")

    def process(self):
       # loading = Loading()
        while Process == 0:
           loading.wait()
        else:
           loading.start_process()
        while (loading.is_Drop_detail):
           loading.Continue()
        loading.Reset()

loading = Loading()
#loading.process()











