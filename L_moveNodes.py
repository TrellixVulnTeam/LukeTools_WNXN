import nuke

SMALLSTEP = 100

LARGESTEP = 400

def moveSel_up(large = False):
	for a in nuke.selectedNodes():
		a.setYpos(int(a.ypos() - (LARGESTEP if large else SMALLSTEP)))
		
def moveSel_down(large = False):
	for a in nuke.selectedNodes():
		a.setYpos(int(a.ypos() + (LARGESTEP if large else SMALLSTEP)))
		
def moveSel_right(large = False):
	for a in nuke.selectedNodes():
		a.setXpos(int(a.xpos() + (LARGESTEP if large else SMALLSTEP)))
		
def moveSel_left(large = False):
	
	for a in nuke.selectedNodes():
		a.setXpos(int(a.xpos() - (LARGESTEP if large else SMALLSTEP)))