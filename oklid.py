import math

# Öklid mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaların tanımlanması
points = [(1, 2), (3, 4), (6, 8), (9, 10)]

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonuçların yazdırılması
print(f"Noktalar arası mesafeler: {distances}")
print(f"Minimum mesafe: {min_distance}")
