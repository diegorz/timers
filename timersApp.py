import logging
import argparse
import time
import math
import curses

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--timeAnalysis", required=True, help="time to analysis")
ap.add_argument("-o", "--output", required=True, help="output file")
args = ap.parse_args()


class Timers:
    """

    """
    def __init__(self):
        log_path_file = str(args.output)
        logging.basicConfig(filename=log_path_file,
                            datefmt='%d-%m-%Y %H:%M:%S',
                            format='%(asctime)s;%(levelname)s;%(message)s',
                            level=logging.DEBUG)

        logging.Formatter.converter = time.gmtime

        self.screen = curses.initscr()
        try:
            curses.noecho()
            curses.curs_set(0)
            self.screen.keypad(1)
            self.screen.addstr("Press left, up or right to start\n")
            self.event = self.screen.getch()
        except Exception as e:
            logging.error(e)

        if self.event in [curses.KEY_LEFT, curses.KEY_UP, curses.KEY_RIGHT]:
            logging.info("Start...")
            self.screen.addstr('Start...\n')
            self.timing()

        else:
            self.screen.addstr("Not valid key to enter\n")

    def timing(self):
        timer1, timer2, timer3, new_time_init = 0, 0, 0, 0
        flag_timer1, flag_timer2, flag_timer3 = False, False, False
        counter_timer1, counter_timer2, counter_timer3 = 0, 0, 0
        init_time = math.trunc(time.time())

        try:
            while math.trunc(time.time()) - init_time <= int(args.timeAnalysis):
                logging.info("TIME: " + str(math.trunc(time.time()) - init_time))

                if self.event == curses.KEY_LEFT:
                    logging.info("Start Timer 1")
                    self.event = self.screen.getch()
                    if self.event == curses.KEY_UP:
                        if flag_timer1 is False:
                            time_timer1 = math.trunc(time.time()) - init_time
                        else:
                            time_timer1 = (math.trunc(time.time())) - new_time_init

                        new_time_init = math.trunc(time.time())
                        timer1 += time_timer1
                        flag_timer2 = True
                        logging.info("Stop Timer 1: " + str(time_timer1))
                        counter_timer1 += 1
                        continue

                    else:
                        self.event = self.screen.getch()
                        pass

                elif self.event == curses.KEY_UP:
                    logging.info("Start Timer 2")
                    self.event = self.screen.getch()
                    if self.event in [curses.KEY_LEFT, curses.KEY_RIGHT]:
                        if flag_timer2 is False:
                            time_timer2 = math.trunc(time.time()) - init_time
                        else:
                            time_timer2 = (math.trunc(time.time())) - new_time_init

                        new_time_init = math.trunc(time.time())
                        timer2 += time_timer2
                        flag_timer1 = True
                        flag_timer3 = True
                        logging.info("Stop Timer 2: " + str(time_timer2))
                        counter_timer2 += 1
                        continue

                    else:
                        self.event = self.screen.getch()
                        pass

                elif self.event == curses.KEY_RIGHT:
                    logging.info("Start Timer 3")
                    self.event = self.screen.getch()
                    if self.event == curses.KEY_UP:
                        if flag_timer3 is False:
                            time_timer3 = math.trunc(time.time()) - init_time
                        else:
                            time_timer3 = (math.trunc(time.time())) - new_time_init

                        new_time_init = math.trunc(time.time())
                        timer3 += time_timer3
                        flag_timer2 = True
                        logging.info("Stop Timer 3: " + str(time_timer3))
                        counter_timer3 += 1
                        continue

                    else:
                        self.event = self.screen.getch()
                        pass

            logging.info("END!")
            logging.info("Timer 1: " + str(timer1) + " seconds, Count: " + str(counter_timer1) + " times")
            logging.info("Timer 2: " + str(timer2) + " seconds, Count: " + str(counter_timer2) + " times")
            logging.info("Timer 3: " + str(timer3) + " seconds, Count: " + str(counter_timer3) + " times")
            self.screen.addstr("END!")
            curses.endwin()

        except Exception as e:
            print("Error: " + str(e))


if __name__ == '__main__':
    Timers()
