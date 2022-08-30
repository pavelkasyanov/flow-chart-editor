from src.elements.base_element import BaseElement


def detect_element_collision(first_element: BaseElement, second_element: BaseElement) -> bool:
    point_a_x = first_element.x
    point_a_y = first_element.y

    point_b_x = point_a_x + first_element.width
    point_b_y = point_a_y

    point_c_x = point_a_x
    point_c_y = point_a_y + first_element.height

    point_d_x = point_a_x + first_element.width
    point_d_y = point_a_y + first_element.height

    if second_element.is_point_in_element(point_a_x, point_a_y):
        return True
    if second_element.is_point_in_element(point_b_x, point_b_y):
        return True
    if second_element.is_point_in_element(point_c_x, point_c_y):
        return True
    if second_element.is_point_in_element(point_d_x, point_d_y):
        return True

    return False
