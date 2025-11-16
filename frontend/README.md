Goals: 
So the goal is to recreate this video: https://www.youtube.com/watch?v=GQbzTweliuc&list=LL&index=4
bcs i thought it was cute <3

Feature List:
- One Page a Day
- History Log to See Passing Journal
- Weekly Overview
- Box for Personal To Do's
- One Line a Day

API endpoints
- idk python flask is hard, im just going to do the typescript first :) 

Component tree
src/
  api/
    journal.ts
    todos.ts
    auth.ts

  components/
    journal/
      DayPage.tsx
      WeekOverview.tsx
      HistoryList.tsx
      OneLine.tsx
    todos/
      TodoList.tsx
      TodoItem.tsx
    ui/
      Button.tsx
      Card.tsx
      TextArea.tsx
      Input.tsx

  pages/
    Today/
      TodayPage.tsx
    History/
      HistoryPage.tsx
    Weekly/
      WeeklyPage.tsx

  context/
    AuthContext.tsx
    JournalContext.tsx

  hooks/
    useJournal.ts
    useTodos.ts
    useAuth.ts

  types/
    journal.ts
    todo.ts
    user.ts

  utils/
    date.ts
    fetcher.ts

  styles/
    globals.css
