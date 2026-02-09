# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sal-kawa <sal-kawa@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/09 20:58:48 by sal-kawa          #+#    #+#              #
#    Updated: 2026/02/09 21:00:58 by sal-kawa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    age = int(input("Enter the age of the plant in years: "))
    if age > 60:
        print("plant is ready to harvest!")
    else:
        print("plant needs more time to grow.")