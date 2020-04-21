from statemachine import StateMachine, State
from Welding_file import Welding
from Unloading_file import Unloading
from Loading_file import Loading

class UpperMachine(StateMachine):
    start =State('Start', initial=True)
    loading = State('Loading')
    welding =State('Welding')
    unloading= State('Unloading')
    end=State('End')

    Start=start.to(loading)
    LtoW=loading.to(welding)
    WtoU=welding.to(unloading)
    UtoL=unloading.to(end)
    Reset=end.to(start)


    def on_enter_loading(self):
        B.process()

    def on_enter_welding(self):
        C.welding_process()

    def on_enter_unloading(self):
        print("Unloading")
        D.unloading_process()

    def on_enter_end(self):
        print("fe")
    #    print("tutaj")
     #   print(B.loadingcurrent_state)
      #  B.Reset()
       # print(B.loadingcurrent_state)
       # B.wait()
        #print(B.loading.current_state)
Machine=UpperMachine()
while(True):
    B=Loading()
    C=Welding()
    D=Unloading()
    Machine.Start()
    print("1.")
    Machine.LtoW()
    print("2.")
    Machine.WtoU()
    print("3.")
    Machine.UtoL()
    print("je")
    Machine.Reset()



