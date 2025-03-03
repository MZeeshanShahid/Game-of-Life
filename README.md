 Conway’s Game of Life

 Programmet holde styr på et spillebrett av en vilkårlig størrelse, der hvert felt i brettet inneholder en celle. En celle kan være levende eller død. 
 Simuleringen utspiller seg over flere generasjoner (velger selv). Hver generasjon fremkommer gjennom at spillebrettet oppdateres jevnlig. En oppdatering skjer ved at celler lever eller dør avhengig av sine omgivelser.
 
 - Dersom cellens nåværende status er **"levende"**:
    - Ved færre enn to levende naboceller dør cellen (**underpopulasjon**).
    - Ved to eller tre levende naboceller vil cellen leve videre.
    - Hvis cellen har mer enn tre levende naboceller vil den dø (**overpopulasjon**).
- Dersom cellen er **"død"**:
    - Cellens status blir **"levende"** (**reproduksjon**) dersom den har nøyaktig tre levende naboer.


    
