# Name:Nikhil Braganza
# Student_ID:29977770
# Start_Date: 28_Oct_2018
# Last_Modified:28_Oct_2018
#               31_Oct_2018
#               2_Oct_2018
#               6_Oct_2018
#               8_Oct_2018
#               9_Oct_2018
#               11_Oct_2018


import matplotlib.pyplot as plot
import task2 as task2


class visualizer:
    def __init__(self, data):
        self.data = data

    def compute_averages(self):
        stat_avg = self.data
        avg_list = []
        for each in stat_avg:
            avg_list.append(each/10)
        print("\naverage statistics:", str(avg_list))
        return avg_list

    def visualise_statistics(self, stats):
        stat_avg = stats
        # comparing the first element of list to determine whether it is td or sli
        if stat_avg[0] == 0:
            del stat_avg[0]  # removing the first element after comparing
            plot.title("average stats for sli children")
            plot.bar(range(len(stat_avg)), stat_avg, label="Specific Language Impairment", color="cyan")
            title = "average stats for sli"
        else:
            del stat_avg[0]  # removing the first element after comparing
            plot.title("average stats for td children")
            plot.bar(range(len(stat_avg)), stat_avg, label="Typical Development", color="red")
            title = "average stats for td"
        labels = ['length', 'size', 'repetition', 'retracing', 'errors', 'pauses']
        plot.xlabel("types of stats (number)")
        plot.ylabel("amount")
        plot.legend()

        plot.xticks(range(len(stat_avg)), labels)
        plot.show()
        print(title, "successfully plotted")


stats = visualizer(task2.Analyser().analyse_script("sli_clean/*.txt")).compute_averages()
sli_obj_vis = visualizer(task2.Analyser().analyse_script("sli_clean/*.txt"))
sli_obj_vis.visualise_statistics(stats)

stats = visualizer(task2.Analyser().analyse_script("td_clean/*.txt")).compute_averages()
td_obj_vis = visualizer(task2.Analyser().analyse_script("td_clean/*.txt"))
td_obj_vis.visualise_statistics(stats)
