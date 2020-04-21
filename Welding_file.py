import time
from statemachine import StateMachine, State

waitTime = [1, 2, 3, 4]
workspaceMatrix = [False, False, False, False]  # niepospawanie , w czasie spawania, popspawanty
welding = ['Welding state', 'Welding turned on', 'Still welding']


def work_wait(i):
    time.sleep(waitTime[i])


class Welding(StateMachine):
    # waitforSignal = State('waiting',initial=True)
    welding = State('welding', initial=True)
    weldingON = State('weldingON', initial=False)
    weldingDone = State('weldingDone', initial=False)

    d_not_welded = welding.to(weldingON)
    started_welding = weldingON.to(welding)
    d_during_welding = welding.to(welding)
    d_welded = welding.to(weldingDone)
    # signal_to_master = weldingDone.to()

    state_being_done = False

    def on_enter_welding(self):
        if self.state_being_done == False:
            state_being_done = True
            if (workspaceMatrix[0] == False and workspaceMatrix[1] == False and workspaceMatrix[2] == False and
                    workspaceMatrix[3] == False):
                print(welding[0])
            if (workspaceMatrix[0] == False and workspaceMatrix[1] == True and workspaceMatrix[2] == False and
                    workspaceMatrix[3] == False):
                print(welding[2])
            if (workspaceMatrix[0] == False and workspaceMatrix[1] == False and workspaceMatrix[2] == True and
                    workspaceMatrix[3] == False):
                print(welding[2])
            work_wait(0)
            state_being_done = False

    def on_enter_started_welding(self):
        if self.state_being_done == False:
            state_being_done = True
            print('Started welding!')
            work_wait(1)
            state_being_done = False

    def on_enter_weldingON(self):
        if self.state_being_done == False:
            state_being_done = True
            print(welding[1])
            work_wait(2)
            state_being_done = False

    def on_enter_weldingDone(self):
        if self.state_being_done == False:
            state_being_done = True
            print('Welding done!')
            work_wait(3)
            state_being_done = False

    # cycle = welding.to(weldingON) | welding.to(welding) | welding.to(weldingDone)

    def welding_process(self):
        stanSpawania = Welding()
        if (workspaceMatrix[0] == False and workspaceMatrix[1] == False and workspaceMatrix[2] == False and workspaceMatrix[3] == False):
            stanSpawania.d_during_welding()
        workspaceMatrix[0] = True;

        if (workspaceMatrix[0] == True and workspaceMatrix[1] == False and workspaceMatrix[2] == False and
                workspaceMatrix[3] == False):
            stanSpawania.d_not_welded()
            workspaceMatrix[0] = False
        workspaceMatrix[1] = True

        if (workspaceMatrix[0] == False and workspaceMatrix[1] == True and workspaceMatrix[2] == False and
                workspaceMatrix[3] == False):
            stanSpawania.started_welding()
            workspaceMatrix[1] = False
        workspaceMatrix[2] = True

        if (workspaceMatrix[0] == False and workspaceMatrix[1] == False and workspaceMatrix[2] == True and
                workspaceMatrix[3] == False):
            stanSpawania.d_during_welding()
            workspaceMatrix[2] = False
        workspaceMatrix[3] = True

        if (workspaceMatrix[0] == False and workspaceMatrix[1] == False and workspaceMatrix[2] == False and
                workspaceMatrix[3] == True):
            stanSpawania.d_welded()
            workspaceMatrix[3] = False


