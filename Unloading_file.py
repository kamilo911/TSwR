from statemachine import StateMachine, State
import time

workspaceMatrix = [False, False, False, False]
waitTime = [1, 2, 3, 4, 5]


def work_wait(i):
    time.sleep(waitTime[i])


class Unloading(StateMachine):
    Check_details = State("Check for details", initial=True)
    Unloading_state = State('State of unloading')
    Begin_unloading = State('Begin unloading')
    Unloading_finished = State('The unloading is finished')

    detail_welded = Check_details.to(Unloading_state)
    not_started = Unloading_state.to(Begin_unloading)
    unloading_begun = Begin_unloading.to(Unloading_state)
    during_unloading = Unloading_state.to.itself()
    finished = Unloading_state.to(Unloading_finished)

    cycle = detail_welded | not_started | unloading_begun | during_unloading | finished

    def on_detail_welded(self):
        print('There is a welded detail on the positioner')
        work_wait(0)

    def on_not_started(self):
        print('The unloading has not begun')
        work_wait(1)

    def on_unloading_begun(self):
        print('The unloading has begun')
        work_wait(2)

    def on_during_unloading(self):
        print('Unloading is in progress')
        work_wait(3)

    def on_finished(self):
        print('The unloading has finished')
        work_wait(4)

    def unloading_process(self):
        Unloading_state = Unloading()
        if (workspaceMatrix[0] == False and workspaceMatrix[1] == False and workspaceMatrix[2]== False and workspaceMatrix[3]==False):
            Unloading_state.detail_welded()
        workspaceMatrix[0] = True

        if (workspaceMatrix[0] == True and workspaceMatrix[1] == False and workspaceMatrix[2]== False and workspaceMatrix[3]==False):
            Unloading_state.not_started()
            workspaceMatrix[0] = False
        workspaceMatrix[1] = True

        if (workspaceMatrix[0] == False and workspaceMatrix[1] == True and workspaceMatrix[2]== False and workspaceMatrix[3]==False):
            Unloading_state.unloading_begun()
            workspaceMatrix[1] = False
        workspaceMatrix[2] = True

        if (workspaceMatrix[0] == False and workspaceMatrix[1] == False and workspaceMatrix[2]== True and workspaceMatrix[3]==False):
            Unloading_state.during_unloading()
            workspaceMatrix[2] = False
        workspaceMatrix[3] = True

        if (workspaceMatrix[0] == False and workspaceMatrix[1] == False and workspaceMatrix[2]== False and workspaceMatrix[3]==True):
            Unloading_state.finished()
            workspaceMatrix[3] = False

#A - sprawdzanie czy są detale, a3 - detal pospawany na pozycjonerze, D - stan rozładunku, d1 - nie rozpoczety, d2 - w trakcie, d3 - zakończony
#d4 - rozpoczety, D1 - rozpocznij rozładunek, D2 - rozładunek zakończony