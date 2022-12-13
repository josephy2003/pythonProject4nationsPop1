import arcade

my_file = open("nationsPop.txt",'r')
lines = my_file.readlines()
country_data = []

for line in my_file:
    countries = (line.split(",")[0])
    population = (line.split(",")[1])
    growth = (line.split(",")[2])
    print(growth)

#in class notes/work~

for country_line in lines:
    country_line = country_line.strip()
    nation_pop_list = country_line.split(',')
    pop_dictionary = {'Name' :nation_pop_list[0],
                      'pop' :int(nation_pop_list[1]),
                      'change' :float(nation_pop_list[2])
                      }
    country_data.append(pop_dictionary)

    #prove that it worked
    for nation in country_data:
        print(nation)

my_window = arcade.open_window(2560,1440)

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()


                #Y line       #height

arcade.draw_line(120, 1400,120,500, arcade.color.BLUE,6)

                #X line

arcade.draw_line(120, 500, 1000, 500, arcade.color.BLUEBERRY, 6)

                #staryx #starty endX  endy

#1
for pop_number in range(300, 1750, 100):
    label = arcade.Text(f"{pop_number}M",5, pop_number, arcade.color.RED_DEVIL)

#2nd
for pop_number in range(100, 3000, 200):
    label = arcade.Text(f"{pop_number}M", 10, pop_number, arcade.color.RED_DEVIL)
    label.draw()

#CHART (RECTS.)
                               #  | X | Y |W | H |
arcade.draw_xywh_rectangle_outline(130,500,100, 350, arcade.color.ANDROID_GREEN, 5)

#bar_height = (int(nation_data[1])-100_000_000)/1_000_000

arcade.finish_render()

arcade.run()