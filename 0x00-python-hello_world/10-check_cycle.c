#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list in the cycle
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *tmp;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	tmp = current->next;
	while (current != NULL && tmp->next != NULL)
	{
		if(current == tmp)
		{
			return (1);
		}
		current = current->next;
		tmp = tmp->next->next;
	}
	return (0);
}

