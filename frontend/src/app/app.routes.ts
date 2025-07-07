import { Routes } from '@angular/router'
import { Home } from './pages/home/home.component'
import { CreateSummary } from './pages/create-summary/create-summary.component'
import { SummaryList } from './pages/summary-list/summary-list.component'

export const routes: Routes = [
  { path: '',       component: Home    }, // /
  { path: 'create', component: CreateSummary },
  { path: 'list',   component: SummaryList  },
  { path: '**',     redirectTo: ''                }
]
