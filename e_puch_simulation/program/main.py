import sim
import sys
import pygame
# import keyboard

pygame.init()
pygame.display.set_mode((200,200))

sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

if clientID != -1:
    print("Connected to remote API server")
else:
    print("Failed to connect to API server")
    sys.exit()

_, left_motor = sim.simxGetObjectHandle(clientID, './leftMotor', sim.simx_opmode_oneshot_wait)
_, right_motor = sim.simxGetObjectHandle(clientID, './rightMotor', sim.simx_opmode_oneshot_wait)

left_speed = 0.0
right_speed = 0.0
max_speed = 2.0

start = True

while sim.simxGetConnectionId(clientID) != -1 and start:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_speed = -max_speed
                right_speed = max_speed
            elif event.key == pygame.K_RIGHT:
                left_speed = max_speed
                right_speed = -max_speed
            elif event.key == pygame.K_UP:
                left_speed = max_speed
                right_speed = max_speed
            elif event.key == pygame.K_DOWN:
                left_speed = -max_speed
                right_speed = -max_speed
            elif event.key == pygame.K_SPACE:
                left_speed = 0.0
                right_speed = 0.0
            elif event.key == pygame.K_q:
                left_speed = 0
                right_speed = 0
                start = False
    # if keyboard.is_pressed('up'):
    #     left_speed = max_speed
    #     right_speed = max_speed
    # elif keyboard.is_pressed('dow'):
    #     left_speed = -max_speed
    #     right_speed = -max_speed
    # elif keyboard.is_pressed('right'):
    #     left_speed = max_speed
    #     right_speed = -max_speed
    # elif keyboard.is_pressed('left'):
    #     left_speed = -max_speed
    #     right_speed = max_speed
    # elif keyboard.is_pressed('space'):
    #     left_speed = 0
    #     right_speed = 0
    
    
    sim.simxSetJointTargetVelocity(clientID, left_motor, left_speed, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, right_motor, right_speed, sim.simx_opmode_oneshot)

sim.simxFinish(clientID)
pygame.quit()
quit()