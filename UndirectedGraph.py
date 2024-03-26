import networkx as nx
import matplotlib.pyplot as plt
import random
import time  # 导入时间模块


def Generate_UndirectedGraph():
    # 创建无向图
    Graph = nx.Graph()

    # 添加60个结点
    max_node_size = 60
    matrix = [[0 for _ in range(max_node_size + 1)] for _ in range(max_node_size + 1)]

    nodes = range(1, 61)
    Graph.add_nodes_from(nodes)

    # 添加边，使得边数为50条
    max_edges = 50
    while len(Graph.edges()) < max_edges:
        # 随机选择两个节点
        node1 = random.choice(nodes)
        node2 = random.choice(nodes)
        # 确保所选节点不相同且之间没有边
        if node1 != node2 and not Graph.has_edge(node1, node2):
            Graph.add_edge(node1, node2)
            # 随机生成权重
            temp = random.randint(1, 9)
            matrix[node1][node2] = temp
            matrix[node2][node1] = temp

    # 使用 spring layout，并自定义 k 参数
    pos = nx.spring_layout(Graph, k=10)  # 设置 k 参数

    # 生成节点的随机浅色
    node_colors = [(random.randint(100, 255) / 255, random.randint(100, 255) / 255, random.randint(100, 255) / 255) for
                   _ in
                   nodes]

    # 绘制无向图
    nx.draw(Graph, pos, with_labels=True, node_color=node_colors, node_size=300, edge_color='grey', linewidths=1,
            font_size=9)

    # 获取当前时间戳
    timestamp = int(time.time())
    # 保存图片到计算机，并使用时间戳命名
    # plt.savefig(f"./graph_{timestamp}.jpg")
    plt.savefig(f"./images/UndirectedGraph/graph_{timestamp}.jpg")
    plt.show()

    # for i in range(1, max_node_size + 1):
    #     for j in range(1, max_node_size + 1):
    #         print(matrix[i][j], end=' ')
    #     print()
