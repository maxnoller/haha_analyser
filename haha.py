import matplotlib.pyplot as plt
import sys

def get_valid_lines(path):
    with open(path, "r", encoding="utf8") as f:
        lines = f.readlines()
        return filter_lines(lines)

def filter_lines(lines):
    filtered_lines = []
    for line in lines:
        if line.endswith("<Media omitted>"):
            continue
        else:
            split_line = line.split(": ")
            if(len(split_line) > 1 and split_line[1].startswith("http")):
                continue
            else:
                filtered_lines.append(line)
    return filtered_lines

def count_categorize_lines(lines):
    nrof_haha = 0
    nrof_xd = 0
    nrof_normal = 0
    for line in lines:
        if line.endswith("xD\n") or line.endswith("xd\n"):
            nrof_xd+=1
        elif(line.endswith("haha\n")):
            nrof_haha+=1
        else:
            nrof_normal+=1
    return nrof_haha, nrof_xd, nrof_normal

def plot_categories(nrof_haha, nrof_xd, nrof_normal):
    labels = "haha", "xd", "Other"
    sizes = [nrof_haha, nrof_xd, nrof_normal]
    fig1, ax1, = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")
    plt.show()

if __name__ == "__main__":
    nrof_haha, nrof_xd, nrof_normal = count_categorize_lines(get_valid_lines(sys.argv[1]))
    plot_categories(nrof_haha, nrof_xd, nrof_normal)