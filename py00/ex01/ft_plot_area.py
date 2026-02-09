# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sal-kawa <sal-kawa@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/09 19:39:02 by sal-kawa          #+#    #+#              #
#    Updated: 2026/02/09 19:41:01 by sal-kawa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    area = length * width
    print(f"The area is: {area}")