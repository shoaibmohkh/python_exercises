# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sal-kawa <sal-kawa@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/09 19:53:15 by sal-kawa          #+#    #+#              #
#    Updated: 2026/02/09 20:07:32 by sal-kawa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    total = 0
    i = 0
    while (i < 3):
        i += 1
        save = int(input(f"Day {i} harvest: "))
        total += save
    print(f"Total harvest: {total}")
    # for (i in range(1, 4)):
    #     print(f"Day {i} harvest: {total}")