Dieser Code ist eine Simulation eines Raketenfluges, der die Höhe, Geschwindigkeit und Beschleunigung der Rakete im Laufe der Zeit berechnet und in drei separaten Graphen mit Hilfe der Bibliothek "plotly" visualisiert.

Zu Beginn des Codes werden die erforderlichen Bibliotheken importiert (math, plotly, pandas) und zwei Klassen (Rocket und Umgebung) definiert. Anschließend werden einige Parameter für die Rakete festgelegt.

Die Simulationsgenauigkeit wird dann vom Benutzer abgefragt, und die maximale Anzahl von Simulationsschritten wird berechnet.

Danach beginnt die Simulation, indem die Position, Geschwindigkeit und Beschleunigung der Rakete in jedem Schritt aktualisiert werden. Die Triebwerkslaufzeit wird ebenfalls aktualisiert, abhängig von der Gesamtlaufzeit und der aktuellen Zeit. Der Luftwiderstand wird auch berücksichtigt und in die Berechnung der Beschleunigung der Rakete einbezogen. Wenn die Rakete den Boden erreicht hat, wird die Simulation beendet und die Ergebnisse werden in Diagrammen dargestellt.

Die drei Diagramme zeigen die Höhe, Geschwindigkeit und Beschleunigung der Rakete im Laufe der Zeit. Der Benutzer wird aufgefordert, die Diagramme anzuzeigen, indem er "y" eingibt.
