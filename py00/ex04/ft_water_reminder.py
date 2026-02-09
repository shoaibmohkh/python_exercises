# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sal-kawa <sal-kawa@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/09 21:04:45 by sal-kawa          #+#    #+#              #
#    Updated: 2026/02/09 21:06:42 by sal-kawa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    last = int(input("Days since last watering: "))
    if (last > 3):
        print("time to water the plant!")
    else:
        print("the plant is still good!")