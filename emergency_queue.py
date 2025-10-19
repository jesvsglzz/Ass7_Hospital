class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []

    def print_heap(self):
        print("\nCurrent Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            current = self.data[index]
            parent = self.data[parent_index]

            if current.urgency < parent.urgency:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left
        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self.heapify_down(smallest)

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()

        min_patient = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return min_patient


# Test your MinHeap class here including edge cases
heap = MinHeap()
heap.insert(Patient("Julio", 3))
heap.insert(Patient("Laura", 1))
heap.insert(Patient("Felipe", 5))
heap.print_heap()

next_up = heap.peek()
if next_up:
    print(f"\nNext patient: {next_up.name} ({next_up.urgency})")

served = heap.remove_min()
print(f"\nServed: {served.name}")
heap.print_heap()