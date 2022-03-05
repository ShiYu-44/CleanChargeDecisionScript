import random
women = ['女性A', '女性B']
members = ['男性A', '男性B', '男性C', '男性D', '男性E', '男性F', '男性G', '男性H', ]
random.shuffle(women)
random.shuffle(members)
print('おめでとうございます！\n女性用お手洗い掃除担当は、' +
      women.pop() + '\n男性用お手洗い掃除担当は、' + members.pop())
members.extend(women)
random.shuffle(members)
print('掃除機担当は' + members[0] +
      '\n机ふき担当は' + members[1])
